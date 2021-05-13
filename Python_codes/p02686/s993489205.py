import sys
sys.setrecursionlimit(100000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():  
    N = int(input())
    flag1 = False
    flag2 = False
    left = 0
    left2 = []
    right = 0
    right2 = []
    for _ in range(N):
        s = input()
        stack = ['-']
        for t in s:
            if t == '(':
                stack.append(t)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
        if len(stack) == 1:
            continue
        elif stack[1] == '(':
            flag1 = True
            left += len(stack) - 1
        elif len(stack) >= 3  and stack[1] == ')' and stack[-1] == '(':
            for i in range(len(stack)):
                if stack[i] == '(':
                    s = i
                    break
            left2.append(len(stack) - s)
            right2.append(s - 1)
        else:
            flag2 = True
            right += len(stack) - 1
    if (right == 0 and left == 0 and  sum(right2) == 0 and sum(left2) == 0):
        print('Yes')
    else:
        l = 0
        if len(left2) > 0:
            l = min(left2)
        r = 0
        if len(right2) > 0:
            r = min(right2)
        x = max(r,l)
        if flag1 and flag2 and (right + sum(right2) == left + sum(left2)) and (left >= x) and (right >= x):
            print('Yes')
        else:
            print('No')
if __name__ == '__main__':
    main()