def codefes17f_a():
    s = str(input())
    if s.replace('A', '') != 'KIHBR': return print('NO')
    if 'AA' in s: return print('NO')
    if not 'KIH' in s: return print('NO')
    return print('YES')

if __name__ == '__main__':
    codefes17f_a()