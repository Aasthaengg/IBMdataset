def repeat_acl(K: int) -> str:
    return "ACL" * K


if __name__ == "__main__":
    K = int(input())
    ans = repeat_acl(K)
    print(ans)
