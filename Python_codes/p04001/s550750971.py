# -*- coding: utf-8 -*-
import itertools

def part_sum(S, clist):
    start = 0
    sum = 0
    for c in clist:
        sum += int(S[start:c])
        start = c
    sum += int(S[start:])
    return sum

def main():
    s = input()
    # output = int(input())
    length = len(s)
    numlist = list(range(1, length))
    ans = 0
    for i in range(length):
        combi = list(itertools.combinations((numlist), i))
        for clist in combi:
            clist = list(clist)
            ans += part_sum(s, clist)
    print(ans)
    # if ans == output:
    #     print('OK')
    # else:
    #     print('No')
                
            
        
    
if __name__ == '__main__':
    main()