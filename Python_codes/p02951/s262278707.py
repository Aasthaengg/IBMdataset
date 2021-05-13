def q1():
    A, B, C = (int(i) for i in input().split())
    ans = C-(A-B)
    if ans < 0:
        ans = 0
    print(ans)

    
if __name__ == '__main__':
    q1()