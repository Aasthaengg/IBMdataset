n = int(input())
l = list(range(111,1000,111))

if n % 111 == 0:
    print(n)
else:
    print(l[n // 111])