import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline()[:-1]
mod = 10**9 + 7
def readInt():return int(input())
def readIntList():return list(map(int,input().split()))
def readStringList():return list(input())
def readStringListWithSpace():return list(input().split())
def readString():return input()

n = readInt()
arr = readIntList()
if len(arr) < 3:
    print("0")
    exit()
arr.sort()
count = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            continue
        for k in range(j+1,n):
            if arr[i] == arr[k] or arr[j] == arr[k]:
                continue
            if arr[i] + arr[j] > arr[k]:
                count += 1
print(count)