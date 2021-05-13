import sys
readline = sys.stdin.buffer.readline

N = int(readline())
S = [readline().rstrip().decode() for _ in range(N)]

def count_cb_ob(s):
    st = []
    for i, si in enumerate(s):
        if si == '(' or len(st) == 0 or st[-1] != '(':
            st.append(si)
        else:
            st.pop()
    return st.count(')'), st.count('(')

cb_obs = list(map(count_cb_ob, S))
f = list(filter(lambda cb_ob: cb_ob[0] < cb_ob[1] , cb_obs))
b = list(filter(lambda cb_ob: cb_ob[0] > cb_ob[1] , cb_obs))
s = list(filter(lambda cb_ob: cb_ob[0] == cb_ob[1] , cb_obs))

f = sorted(f)
b = sorted(b, key=lambda x:x[1], reverse=True)

count = 0
ans = 'Yes'
for down, up in (*f, *s, *b):
    count -= down
    if count < 0:
        ans = 'No'
    count += up

if count != 0:
    print('No')
else:
    print(ans)