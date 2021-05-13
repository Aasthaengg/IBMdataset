def main():
    n=int(input())
    m=int((2*n)**0.5)
    if m*(m+1)==n*2:
        print("Yes")
        m+=1
        print(m)
    else:
        print("No")
        exit()
    
    ans=[[m-1] for i in range(m)]
    c=1
    for i in range(m):
        for j in range(i+1,m):
            ans[i].append(c)
            ans[j].append(c)
            c+=1
    for i in ans:
        print(" ".join(map(str,i)))


if __name__ == '__main__':
    main()






