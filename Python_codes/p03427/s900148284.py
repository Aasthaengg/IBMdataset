def digitsum(N):
    return sum(map(int,list(str(N))))
N = int(input())
print(max(digitsum(N),int(str(N)[0])-1+9*(len(str(N))-1)))