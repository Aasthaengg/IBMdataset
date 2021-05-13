def get(s,t):
    return s // (10 ** (t - 1)) % 10


A,B = map(int,input().split())

count = 0

for i in range(A,B+1):
    one = get(i,1)
    two = get(i,2)
    four = get(i,4)
    five = get(i,5)

    if one == five and two == four:
        count += 1

print(count)