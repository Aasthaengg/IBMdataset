A, B, C = map(int, input().split())

first_amari = A%B
next_amari=0
i=2
while(first_amari!=next_amari):
    next_amari = (A*i) % B
    if next_amari == C:
        print("YES")
        exit()
    i+=1

print("NO")