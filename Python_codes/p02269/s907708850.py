# ALDS1_4_C.
# ハッシュテーブル。

def get_key(_str):
    key = 0
    for i in range(len(_str)):
        if _str[i] == 'A': key += 1
        elif _str[i] == 'C': key += 2
        elif _str[i] == 'G': key += 3
        elif _str[i] == 'T': key += 4
        key *= 5
    return key
    
def main():
    n = int(input())
    dict = {}
    for i in range(n):
        command = input().split()
        if command[0][0] == 'i':
            dict[get_key(command[1])] = command[1]
        else:
            key = get_key(command[1])
            if key in dict: print('yes')
            else: print('no')
    
if __name__ == "__main__":
    main()

