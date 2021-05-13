ABC = list(map(int,input().split()))

sorted_ABC = sorted(ABC,reverse=True)

S = sorted_ABC[0] * 10 +  sorted_ABC[1] + sorted_ABC[2]

print(S)
