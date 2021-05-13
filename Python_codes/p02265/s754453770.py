# -*- coding: utf-8 -*-
from sys import stdin
import collections

class DoublyLinkedList_deque:
    def __init__(self):
        self.doubly_linked_list = collections.deque()

    def execute(self,cmd, key):
        if cmd == 'insert':
            self.doubly_linked_list.appendleft(key)
        elif cmd == 'delete':
            try:
                self.doubly_linked_list.remove(key)
            except:
                pass
        elif cmd == 'deleteFirst':
            self.doubly_linked_list.popleft()
        elif cmd == 'deleteLast':
            self.doubly_linked_list.pop()
        else:
            print("invalid cmd")

n = int(stdin.readline().rstrip())
obj_dll = DoublyLinkedList_deque()
for i in range(n):
    input_str=stdin.readline().rstrip().split()
    cmd = input_str[0]
    x = input_str[1] if len(input_str)>1 else None
    obj_dll.execute(cmd,x)
else:
    print(*obj_dll.doubly_linked_list)

