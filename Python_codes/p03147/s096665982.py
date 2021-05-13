def separate(array,separator):
    results = []
    a = array[:]
    i = 0
    while i<=len(a)-len(separator):
        if a[i:i+len(separator)]==separator:
            results.append(a[:i])
            a = a[i+len(separator):]
            i = 0
        else:
            i+=1
    results.append(a)
    return results


def find(ar):

    if ar==[0]*len(ar):
        return 0
    m=999999999999999
    for i in range(len(ar)):
        if ar[i]<m:
            m=ar[i]
    for i in range(len(ar)):
        ar[i]-=m
    ans=m
    new=separate(ar,[0])
    for i in new:
        ans+=find(i)
    return ans








n=int(input())
ar=[int(i) for i in input().strip().split(" ")]
print(find(ar))


