import copy
def cd_generator(num):
    ans=[]
    for i in range(1,10000000):
        if num%i==0:
            ans.append(i)
    temp=copy.deepcopy(ans)
    temp.reverse()
    for ele in temp:
        ans.append(num//ele)
    return ans
def main():
    n,m=map(int,input().split())
    array=cd_generator(m)
    ans=0
    for ele in array:
        if m//ele>=n:
            ans=max(ans,ele)
    print(ans)
main()