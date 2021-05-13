#!/usr/bin/env python3
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
ans = []

def dfs(arr, max_val):
    if len(arr) == n:
        ans.append(arr)
        return
    for i in range(max_val + 2):
        next_arr = arr[:]
        next_arr.append(i)
        dfs(next_arr, max(max_val, i))

dfs([0], 0)

ans.sort()
orda = ord("a")
for line in ans:
    print("".join([chr(orda + item) for item in line]))