Input = input()

v_lakes =[]  #個々の湖の面積管理用のstack
idx_stack = [] #地形のindex管理用のstack

for i, c in enumerate(Input):
    if c == "\\":
        idx_stack.append(i)
    elif c == "/" and idx_stack:
        j = idx_stack.pop()
        v = i - j

        while v_lakes and j < v_lakes[-1][0]:
            v += v_lakes.pop()[1]

        v_lakes.append((j,v))

ans = [len(v_lakes)]
v = [v[1] for v in v_lakes]
ans.extend(v)

print(sum(v))
print(*ans)
