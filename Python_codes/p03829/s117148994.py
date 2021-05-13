nums1 = [int(e) for e in input().split()]
nums2 = [int(t) for t in input().split()]
ans = 0
N = nums1[0]
A = nums1[1]
B = nums1[2]
for i in range(0,N-1):
    if(nums2[i+1]-nums2[i])*A > B:
        ans+=B
    else:
        ans+=(nums2[i+1]-nums2[i])*A
print(ans)