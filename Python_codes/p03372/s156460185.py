mininf = 0

def cumsum(inlist):
    s = 0
    outlist = []
    for i in inlist:
        s += i
        outlist.append(s)
    return outlist

def maxtohere(inlist):
    s = mininf
    outlist = []
    for i in inlist:
        s = max(s, i)
        outlist.append(s)
    return outlist

n, length = [int(v) for v in input().split()]
sushi = [[int(v) for v in input().split()] for i in range(n)]

diff_distance_from_left = [sushi[i][0] - sushi[i-1][0] if i > 0 else sushi[0][0] for i in range(n)]
diff_distance_from_right = [sushi[i+1][0] - sushi[i][0] if i < n-1 else length - sushi[i][0] for i in range(n-1,-1,-1)]
sushi_oneway_from_left = [sushi[i][1]-diff_distance_from_left[i] for i in range(n)]
sushi_oneway_from_right = [sushi[-i-1][1] - diff_distance_from_right[i] for i in range(n)]
sushi_roundtrip_from_left = [sushi[i][1]-diff_distance_from_left[i]*2 for i in range(n)]
sushi_roundtrip_from_right = [sushi[-i-1][1] - diff_distance_from_right[i]*2 for i in range(n)]

sum_of_sushi_oneway_from_left = cumsum(sushi_oneway_from_left)
sum_of_sushi_roundtrip_from_left = cumsum(sushi_roundtrip_from_left)
sum_of_sushi_oneway_from_right = cumsum(sushi_oneway_from_right)
sum_of_sushi_roundtrip_from_right = cumsum(sushi_roundtrip_from_right)

sum_of_sushi_oneway_from_left = maxtohere(sum_of_sushi_oneway_from_left)
sum_of_sushi_roundtrip_from_left = maxtohere(sum_of_sushi_roundtrip_from_left)
sum_of_sushi_oneway_from_right = maxtohere(sum_of_sushi_oneway_from_right)
sum_of_sushi_roundtrip_from_right = maxtohere(sum_of_sushi_roundtrip_from_right)

sum_of_sushi_from_left = sum_of_sushi_oneway_from_left
sum_of_sushi_from_right = sum_of_sushi_oneway_from_right
for i in range(n-1):
    sum_of_sushi_from_left[i] += sum_of_sushi_roundtrip_from_right[-2-i]
for i in range(n-1):
    sum_of_sushi_from_right[i] += sum_of_sushi_roundtrip_from_left[-2-i]

print(max(sum_of_sushi_from_left+sum_of_sushi_from_right))