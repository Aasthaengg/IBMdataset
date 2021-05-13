input = list(map(int,input().split()))

h1 = input[0]
m1 = input[1]
h2 = input[2]
m2 = input[3]
k = input[4]

print(h2*60+m2-h1*60-m1-k)
