n = int(input())

def dfs(a, used=0):
    if len(a)==n:
        print(''.join(a))
    else:
        for i in range(ord('a'), ord('a')+used+1):
            if i == ord('a')+used:
                dfs(a+[chr(i)], used+1)
            else:
                dfs(a+[chr(i)], used)

dfs([], 0)
