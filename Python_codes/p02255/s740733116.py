def insertionSort(_list, _length):
    for i in range(1, _length):
        ll = [str(_l) for _l in _list]
        print(' '.join(ll))
        val = _list[i]
        j = i - 1
        while j >= 0 and _list[j] > val:
            _list[j+1] = _list[j]
            j -= 1
        _list[j+1] = val
    ll = [str(_l) for _l in _list]
    print(' '.join(ll))


length = int(input())
eles = list(map(int, input().split()))

insertionSort(eles, length)