w=input();n=int(input())
print(sorted({w[j:j+i+1] for i in range(n) for j in range(len(w)-i)})[n-1])