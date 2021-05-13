conb_list = [ [ 1 for i in range(51) ] for j in range(51) ]
for i in range(1,51):
    for j in range(1,51):
        conb_list[i][j] = conb_list[i-1][j] + conb_list[i][j-1]


n, a, b = [ int(v) for v in input().split() ]
num_list = sorted([ int(v) for v in input().split() ], reverse = True)

def mean(inlist):
    return sum(inlist) / len(inlist)

ans = 0
for i in range(a,b+1):
    if i == a:
        min_element = num_list[i-1]
        min_element_count = num_list.count(min_element)
        min_element_index = num_list.index(min_element)
        max_mean = mean(num_list[:i])

        ans += (conb_list[min_element_count - i + min_element_index][i - min_element_index])
    else:
        if max_mean > mean(num_list[:i]):
            break
        else:
            ans += (conb_list[min_element_count - i + min_element_index][i - min_element_index])

print(max_mean)    
print(ans)
