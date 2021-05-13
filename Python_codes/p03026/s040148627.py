
#https://atcoder.jp/contests/m-solutions2019/submissions/5730635



#x = [1,2,3]
#while x:
#    if x : 
#        print(x)
#        x.pop()


n = int(input())

abn = [list(map(int,input().split())) for _ in range(n-1)]

cn = list( map(int, input().split()) )
cn.sort(reverse = True)


links = [set() for _ in range(n)]

for abi in abn:
    a, b = abi

    a -= 1; b-=1
    links[a].add(b)
    links[b].add(a)



# points of vertices
pv = [0]*n
ans = 0


#リンクを嘗めてsizeが1のもののindexだけ選ぶ
leaves = { i for i, l in enumerate(links) if len(l) == 1 }

# print(*abn)
# print(*cn)
# print(*leaves)
while leaves:
    
    index = leaves.pop()
    cmax = cn.pop()#popなので最小値から利用していく=>大きな値が残っていく
    
    pv[index] = cmax

    if not cn: # 最後のcmax (= 与えられた数列cnの最大値 )を加算する前に抜ける
        break

    ans += cmax
    for ci in links[index]:
        lu = links[ci]
        lu.remove(index)
        if len(lu) == 1:
            leaves.add(ci)

print(ans)
print(*pv)
