import sys
input = sys.stdin.readline
n = int(input())
s = tuple(map(lambda x: ord(x) - ord("a") + 1, input()))
base = 1007
mod = 2**61 - 1

length = n//2
b = [1] * (length + 1)
shash = [0] * (length+1)
for i in range(1, length + 1):
    b[i] = b[i-1] * base % mod
    shash[i] = (shash[i - 1] * base + s[i - 1]) % mod

for ans in reversed(range(1, length+1)):
    # calc hash
    hash_ = 0
    check = {}
    #y = set([])
    for left in range(n - ans + 1):
        if left == 0:
            hash_ = shash[ans]
            check[hash_] = left
            #y.add(hash_)
        else:
            hash_ = base * hash_ - b[ans] * s[left - 1] + s[left + ans - 1]
            hash_ %= mod
            if hash_ in check.keys():
                # print("tmp = ", tmp)
                if check[hash_] <= left - ans:
                    print(ans)
                    # a = check[hash_][tmp-1]
                    # at = "".join(map(lambda x: chr(x + ord("a")), s[a:a+ans]))
                    # for j in range(ans):
                        # if s[a+j] != s[left+j]:
                            # print("Fail")
                            # exit()
                    # print("Success")
                    sys.exit()
            else:
                check[hash_] = left
                #y.add(hash_)
        # print(hash_, s[left:left+ans])
print(0)

