def main():
    n,k=map(int, input().split())
    s= input()
    blocks = []
    nums = []
    tmp  = s[0]
    for i in range(1,n):
        if(s[i]==s[i-1]):
            tmp += s[i]
        else:
            blocks.append(tmp)
            nums.append(len(tmp))
            tmp = s[i]
        if(i==(n-1) and len(tmp)>0):
            blocks.append(tmp)
            nums.append(len(tmp))

    j = len(blocks)
    count = 0
    ans = 0
    for i in range(1,j,2):
        blocks[i] = (blocks[i-1][0])*len(blocks[i])
        count+=1
        if count == k:
            break
    sames = 2*(k)+1

    if(sames >= len(blocks)):
        ans = (n-1)
    else:
        for i in range(sames):
            ans += nums[i]
        ans -= 1
        for i in range(sames,len(blocks)):
            ans+=len(blocks[i])-1
    print(ans)



if __name__ == '__main__':
    main()
