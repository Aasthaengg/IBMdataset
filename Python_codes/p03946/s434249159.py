N,T = map(int,input().split())
A = list(map(int,input().split()))
ar = A[::-1]
maxa = ar[0]
diff = 0
count = 0
for i in ar:
    if maxa < i:
        maxa = i
    else:
        if maxa - i == diff:
            count += 1
        elif maxa - i > diff:
            count = 1
            diff = maxa -i
print(count)