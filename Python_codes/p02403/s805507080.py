import sys

l = sys.stdin.readlines()[:-1]
for i in l:
    h,w = map(int,i.strip().split())
    print(("#"*w+"\n")*h)