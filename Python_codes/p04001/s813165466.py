# coding: utf-8
# Your code here!




def insert_str(target, i, char):
    return target[:i] + char + target[i:]

def calc(target, i):
    global ans
    if i >= len(target):
        ans += eval(target)
        return
    calc(target, i+1)
    calc(insert_str(target, i, "+"), i+2)
        
S = input()
N = len(S)
ans = 0
calc(S, 1)


print(ans)




