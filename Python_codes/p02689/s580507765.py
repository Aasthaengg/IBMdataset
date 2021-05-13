# coding: utf-8
# Your code here!
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    h_list = list(map(int, input().split()))
    d = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        d[a].append(h_list[b-1])
        d[b].append(h_list[a-1])
    
    count = 0
    for i, h in enumerate(h_list):
        if len(d[i+1]) == 0:
            count += 1
            continue
        max_h = max(d[i+1])
        if max_h < h:
            count += 1
    
    print(count)
    
main()
