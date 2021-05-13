def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])
def sortx(x,n,k):
    if k == 0:x.sort(key=lambda y:y[1,n])
    else:x.sort(reversed=True, key=lambda y:y[1,n])

def main():
    s = input()
    NG = 1
    NP = 0
    did = ["g"]
    point = 0
    for i in range(1,len(s)):
        if s[i] == "g":
            if NP + 1 <= NG:
                did.append("p")
                NP += 1
                point += 1
            else:
                did.append("g")
                NG += 1
        else:
            if NP + 1 <= NG:
                did.append("p")
                NP += 1
            else:
                did.append("g")
                NG += 1
                point -= 1
    print(point)

if __name__ == "__main__":
    main()