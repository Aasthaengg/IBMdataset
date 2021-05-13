# coding: utf-8
# ハッシュ（Dictパターン）

hash_list = {}

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        command, arg = input().split()

        if command == 'insert':
            hash_list[arg] = 1
        else:
            print('yes' if arg in hash_list else 'no')
