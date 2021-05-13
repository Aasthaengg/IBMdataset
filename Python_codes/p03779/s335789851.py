n = int(input())
for i in range(1, 2*10**5):
    score = (i*(i+1))//2
    if score >= n:
        print(i)
        exit()
