import sys
input = sys.stdin.readline

k=int(input())
s=input().rstrip()

print(s if len(s)<= k else s[:k]+'...')
