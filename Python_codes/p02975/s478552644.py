from collections import Counter
n = int(input())
c = Counter(map(int, input().split()))
def main():
    # 全部ゼロ
    if c[0] == n:
        ok = True
        return ok
    if n % 3 != 0:
        ok = False
        return ok
    # ゼロとその他1個でかつぜろが1/3個
    if c[0] == n // 3 and len(c) == 2:
        ok = True
        return ok
    # 全部違ってて1/3ずつでxorして0
    if len(c) != 3:
        ok = False
        return ok
    xor = 0
    for x in c:
        if c[x] != n // 3:
            ok = False
            return ok
        xor ^= x
    if xor == 0:
        ok = True
    else:
        ok = False
    return ok
        
if __name__ == '__main__':
    print("Yes" if main() else "No")