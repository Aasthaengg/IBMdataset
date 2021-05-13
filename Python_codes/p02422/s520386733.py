#!/usr/bin/env python

string = input()

n = int(input())

for i in range(n):
    command = input().split()
    if "replace" in command:
        string = string[:int(command[1])] + command[3] + string[int(command[2]) + 1:]
    elif "reverse" in command:
        toReverse = string[int(command[1]):int(command[2]) + 1]
        theReverse = ""
        for i in range(len(toReverse)):
            theReverse += toReverse[-(i + 1)]
        string = string[:int(command[1])] + theReverse + string[int(command[2]) + 1:]
    else:
        print(string[int(command[1]):int(command[2]) + 1])