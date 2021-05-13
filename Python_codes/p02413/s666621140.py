def trans(A):
    """????¬??????????????????¢???"""
    return list(map(list, zip(*A)))

if __name__ == '__main__':
    r, c = [int(i) for i in input().split()]
    sheet = [[int(i) for i in input().split()] for y in range(r)]
    [sheet[y].append(sum(sheet[y])) for y in range(r)]
    sheet = trans(sheet)
    [sheet[y].append(sum(sheet[y])) for y in range(c+1)]
    sheet = trans(sheet)
    [print(' '.join([str(i) for i in sheet[y]])) for y in range(r+1)]