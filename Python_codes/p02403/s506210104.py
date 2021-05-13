ans = []
for line in open(0).readlines():
    H, W = map(int, line.split())
    if not H:
        break
    ans.append((("#"*W)+"\n")*H)
    ans.append("\n")
open(1, 'w').writelines(ans)

