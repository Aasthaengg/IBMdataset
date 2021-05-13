import sys

class DoublyLinkedList:
    def __init__(self, value = -1):
        self.value = value
        self.prev = self
        self.next = self

    def insert(self, value):
        newNode = DoublyLinkedList(value)
        newNode.next = self.next
        newNode.prev = self
        self.next.prev = newNode
        self.next = newNode

    def delete(self, value):
        node = self.next
        while node.value != -1:
            if node.value == value:
                node.next.prev = node.prev
                node.prev.next = node.next
                break
            node = node.next

    def deleteFirst(self):
        if self.next.value != -1:
            self.next = self.next.next
            self.next.prev = self

    def deleteLast(self):
        if self.prev.value != -1:
            self.prev = self.prev.prev
            self.prev.next = self

    def printAll(self):
        node = self.next
        while node.next.value != -1:
            print node.value,
            node = node.next
        print node.value

if __name__ == "__main__":
    dll = DoublyLinkedList()
    lines = sys.stdin.readlines()
    lines.pop(0)
    for line in lines:
        if line[0] == "i":
            dll.insert(int(line[7:]))
        elif line[6] == "F":
            dll.deleteFirst()
        elif line[6] == "L":
            dll.deleteLast()
        else:
            dll.delete(int(line[7:]))
    dll.printAll()