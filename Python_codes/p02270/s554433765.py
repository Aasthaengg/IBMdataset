n, k = map(int, input().split())
a = [int(input()) for i in range(n)]

def check(a, p):
    if max(a) > p:
        return False
    else:
        tr = 0
        count = 1
        for i in a:
            tr += i
            if tr > p:
                count += 1
                tr = i
        if count > k:
            return False
        else:
            return True
Min = 0
Max = max(a) * (n // k + 1)

while Min + 1 < Max:
    if check(a, (Min + Max) // 2) == True:
        Max = (Min + Max) // 2
    else:
        Min = (Min + Max) // 2
print(Max)

