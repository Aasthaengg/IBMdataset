x, n = map(int, input().split())
p = list(map(int, input().split()))
def main():
    for i in range(x+2):
        for j in [-1, 1]:
            ans = x + j*i
            if ans in p:
                continue
            else:
                return ans
        
print(main())        