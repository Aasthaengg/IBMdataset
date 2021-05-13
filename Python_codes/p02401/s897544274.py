while True:
    _exp = raw_input()
    if "?" in _exp:
        break
    print(eval(_exp))