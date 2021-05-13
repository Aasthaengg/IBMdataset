N = int(input())
nums = [int(e) for e in input().split()]
nums.sort()
t=1
ans = 1
t = 10**9
t+=7
i=1
k=0
if(N%2)==1:
    if(nums.count(0) == 1):
        while(i<N):
            if nums[i] == nums[i+1]:
                i+=2
                ans = (ans *2)%t
                continue
            else:
                print('0')
                break
        else:
            print(ans)
    else:
        print('0')
else:
    while(k<N):
        if nums[k] == nums[k+1]:
            k += 2
            ans = (ans * 2)%t
            continue
        else:
            print('0')
            break
    else:
        print(ans)