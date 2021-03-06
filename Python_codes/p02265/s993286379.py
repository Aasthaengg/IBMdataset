#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' ???????????£???????????? '''

from collections import deque

functions = {"insert": lambda obj, x: obj.insert(x),
             "delete": lambda obj, x: obj.delete(x),
             "deleteFirst": lambda obj: obj.deleteFirst(),
             "deleteLast": lambda obj: obj.deleteLast()}


class DoublyLinkedList(object):
    """ Doubly Linked List """

    def __init__(self):
        # self.list = []
        self.list = deque()

    def insert(self, x):
        """ ???????????????x?????????????´?????????\ """
        # self.list = [x] + self.list
        self.list.appendleft(x)

    def delete(self, x):
        """ ??????x??????????????????????´?????????? """
        # for i in range(len(self.list)):
        #     if self.list[i] == x:
        #         self.list.pop(i)
        #         break
        if x in self.list:
            self.list.remove(x)

    def deleteFirst(self):
        """ ?????????????????????????´?????????? """
        # self.list.pop(0)
        self.list.popleft()

    def deleteLast(self):
        """ ????????????????°????????´?????????? """
        self.list.pop()


if __name__ == '__main__':
    N = int(input())

    q = deque()
    for i in range(N):
        command = input().split()
        if command[0] == 'insert':
            q.appendleft(command[1])
        elif command[0] == 'delete':
            if command[1] in q:
                q.remove(command[1])
        elif command[0] == 'deleteFirst':
            q.popleft()
        elif command[0] == 'deleteLast':
            q.pop()

    print(' '.join(map(str, q)))

    # dll = DoublyLinkedList()
    # for i in range(N):
    #     command = input().split()
    #     if len(command) == 1:
    #         functions[command[0]](dll)
    #     elif len(command) == 2:
    #         functions[command[0]](dll, int(command[1]))
    # print(' '.join(map(str, dll.list)))