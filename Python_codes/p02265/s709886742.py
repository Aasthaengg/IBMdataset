from collections import deque
class DoublyLinkedKist:
    DLlist = deque()

    def command(self, cmd):
        if cmd[0] == 'insert':
            self.DLlist.appendleft(cmd[1])
        elif cmd[0] == 'delete':
            if cmd[1] in self.DLlist:
                self.DLlist.remove(cmd[1])
        elif cmd[0] == 'deleteFirst':
            self.DLlist.popleft()
        elif cmd[0] == 'deleteLast':
            self.DLlist.pop()

if __name__ == '__main__':
    DL = DoublyLinkedKist()
    for i in range(int(input())):
        DL.command(input().split())
    print(*DL.DLlist)