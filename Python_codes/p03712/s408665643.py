from collections import deque 
H,W = map(int,input().split())
st = [str(input()) for _ in range(H)]
#print(st)
st = deque(st)
for i in range(H):
    st[i] = '#'+st[i]+'#'
st.appendleft('#'*(W+2))
st.append('#'*(W+2))

for i in range(H+2):
    print(st[i])