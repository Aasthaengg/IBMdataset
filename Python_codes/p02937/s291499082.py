import bisect
s = input()
s_li = list(s)
ma = {}
for i,each_s in enumerate(s_li):
    if each_s not in ma:
        ma[each_s] = [i]
    else:
        ma[each_s].append(i)
t = input()
t_li = list(t)
#print(ma,s_li,t_li)

repeat_count = 0
last_index = -1
for tt in t_li:
    if tt not in ma:
        print(-1)
        exit()
    tmp_li = ma[tt]
    #print(tmp_li)

    lee = len(s_li)
    #add_li = [ii+lee for ii in tmp_li]
    #new_li = tmp_li + add_li
    #bi = bisect.bisect_left(new_li, last_index+1)
    bi = bisect.bisect_left(tmp_li, last_index+1)
    #print(bi,len(tmp_li),'bi',tmp_li,last_index,'last_index')
    if bi>= len(tmp_li):
        repeat_count += 1
        min_index = tmp_li[0]
    else:
        min_index = tmp_li[bi]
    #print(new_li,last_index+1,min_index,'min')
    #if min_index>= lee:
    #    repeat_count += 1
    #    min_index -= lee
    last_index = min_index
    #print(repeat_count,'repeat')
    #print(last_index,'last')
print(lee*(repeat_count)+last_index+1)