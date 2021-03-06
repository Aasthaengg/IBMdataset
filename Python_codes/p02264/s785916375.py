class MyQueue(object):
    """
    My Queue class

    Attributes:
        queue: queue
        head
        tail
    """

    def __init__(self):
        """Constructor
        """
        self.length = 100010
        self.queue = []
        counter = 0
        while counter < self.length:
            self.queue.append(Process())
            counter += 1
        self.head = 0
        self.tail = 0

    def enqueue(self, name, time):
        """enqueue method

        Args:
            name: enqueued process name
            time: enqueued process time

        Returns:
            None
        """
        if self.is_full():
            print("[ERROR] Queue Overflow")
        else:
            self.queue[self.tail % self.length].name = name
            self.queue[self.tail % self.length].time = time
            self.tail += 1

    def dequeue(self):
        """dequeue method

        Returns:
            None
        """
        if self.is_empty():
            print("[ERROR] Queue Underflow")
        else:
            self.queue[self.head % self.length].name = ""
            self.queue[self.head % self.length].time = 0
            self.head += 1

    def is_empty(self):
        """check queue is empty or not

        Returns:
            Bool
        """
        if self.head == self.tail:
            return True
        else:
            return False

    def is_full(self):
        """chech whether queue is full or not"""
        if self.tail - self.head >= len(self.queue):
            return True
        else:
            return False


class Process(object):
    """process class
    """

    def __init__(self, name="", time=0):
        """constructor
        Args:
            name: name
            time: time
        """
        self.name = name
        self.time = time

    def forward_time(self, time):
        """time forward method

        Args:
            time: forward time interval

        Returns:
            remain time

        """
        self.time -= time
        return self.time


def time_forward(my_queue, interval, current_time):
    """

    Args:
        my_queue: queue
        interval: time step interval
        current_time: current time
    """

    value = my_queue.queue[my_queue.head % my_queue.length].forward_time(interval)
    if value <= 0:
        current_time += (interval + value)
        print my_queue.queue[my_queue.head % my_queue.length].name, current_time
        my_queue.dequeue()


    # elif value == 0:
    #     current_time += interval
    #     print my_queue.queue[my_queue.head % my_queue.length].name, current_time
    #     my_queue.dequeue()

    elif value > 0:
        current_time += interval
        name, time = my_queue.queue[my_queue.head % my_queue.length].name, \
                     my_queue.queue[my_queue.head % my_queue.length].time
        my_queue.dequeue()
        my_queue.enqueue(name, time)

    return current_time


my_queue = MyQueue()
n, q = [int(x) for x in raw_input().split()]
counter = 0
while counter < n:
    name, time = raw_input().split()
    my_queue.enqueue(name, int(time))
    counter += 1

current_time = 0
while not my_queue.is_empty():
    current_time = time_forward(my_queue, q, current_time)