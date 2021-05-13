from collections import deque

n = int(input())
dict = {}
for i in range(n):
    order = input().split()
    if order[0] == "insert":
        dict[order[1]] = i
    else:
        if order[1] in dict:
            print("yes")
        else:
            print("no")