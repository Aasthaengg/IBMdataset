n = int(input())

hyo = [[[1]]]

for i in range(n-1):
    n_hyo = []
    for arr in hyo[i]:
        for j in range(max(arr)+1):
            n_arr = arr[:]
            n_arr.append(j+1)
            n_hyo.append(n_arr)
    hyo.append(n_hyo)

alp = ['a','b','c','d','e','f','g','h','i','j']

for i in hyo[n-1]:
    ans = ''
    for j in i:
        ans += alp[j-1]
    print(ans)

    
