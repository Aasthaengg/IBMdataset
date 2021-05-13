def main():
    n=int(input())
    ans=[0]*8
    other = 0
    for a in map(int,input().split()):
        if a >= 3200:
            other+=1
        else:
            ans[a//400] = 1
    a = ans.count(1)
    print(a if a != 0 else 1, a+other)
    
if __name__ == "__main__":
    main()